*<div align="right"> Vikram Procter | June 29 to July 30, 2025 </div>*

# Keep Talking and No One Explodes - Inspired Fake Bomb PCB Design

## Purpose Overview
-   A fun project to learn a new micro controller, and hopfully use some hardware logic
-   A great prank to place in your friends locker
-   A fun game to play with friends

## TODO:
-   Test points for I2C and serial for led controller
-   Add graphics

## Overview:
### <a href="#difusal-modules-details" style="color:inherit">Difusal Modules:</a>
-   Wires
-   Red Button
-   Maze/LED array

### <a href="#display-modules-details" style="color:inherit">Display Modules:</a>
-   Strikes display
-   7-Segment Count down timer
-   Buzzer/Beeper
-   Dramatic LEDs
-   Fake Batteries

### <a href="#expansion-interface-details" style="color:inherit">Expansion Interface:</a>
-   4-Wire Connection containing: power, ground, and two data lines
-   Theoretically one one data line for the binary diffused state could be used

### <a href="#microprocessor-specs" style="color:inherit">Microprocessor</a>:
-	[STM32L412CB processor](https://www.digikey.ca/en/products/detail/stmicroelectronics/STM32L412CBT6/9656217)
-	[8Mhz ABLS-8.000MHZ-B2-T Oscillator](https://www.digikey.ca/en/products/detail/abracon-llc/ABLS-8-000MHZ-B2-T/675284)



## Module Specs:

### Wires Module
-   Two 6 position screw terminals will be used to hold 6 wires
-   Through cuting the correct wires in the correct sequence an LED inidcator next to the module will light green
-   Each wire will connect to ground and the GPIO pins will have an external pullup (3V3)
-   Use two [3 position terminal](https://www.digikey.ca/en/products/detail/phoenix-contact/1988817/950893) to produce one 6 position

### Red Button Module
-   Small red button with colour [light indicator](https://www.digikey.ca/en/products/detail/cree-led/CLMVC-FKA-CL1D1L71BB7C3C3/4794065) next to it.
-   Based on colour and pattern of light the button should be clicked or held
-   The light indicator will indicate if it has been diffused
-   [Tactile push button](https://www.digikey.ca/en/products/detail/te-connectivity-alcoswitch-switches/FSM103/701085), with [red cap](https://www.digikey.ca/en/products/detail/omron-electronics-inc-emc-div/B32-1380/9702) or [yellow cap](https://www.digikey.ca/en/products/detail/omron-electronics-inc-emc-div/B32-1330/9741) 
-   External Pull up

### Maze/LED Array Module
-   The led array will be the Adafruit Industries LLC LED CHARLIEPLEXED MATRIX-9X16 [2974](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/2974/5959351)
-   This array can be controlled using the [IS31FL3731-SALS2-TR](https://www.digikey.ca/en/products/detail/lumissil-microsystems/IS31FL3731-SALS2-TR/14308358?) LED Driver
    - Max current per led can be set using Rext, using Rext=20k, max current per led is 3.2mA
-   LED driver uses I2C meaning only 4 wires is necessary from micro controller
-   Four buttons will be placed around it for control

### Strikes Display Module
-   3D printed case with the three X marks cut out
-   Three LEDs will be placed behind each X, some diffusion film (paper or wax paper) could be used
-   LEDs [LTST-C170KAKT](https://www.digikey.ca/en/products/detail/liteon/LTST-C170KAKT/386773?s=N4IgTCBcDaIDIBUDKCC0BhAjAdgAwGkBBfBEAXQF8g) will be connected to the LED controller used for RGB status LEDs

### 7-Segment Countdown Timer Module
-   Use a 4 character [TDCR1060M](https://www.digikey.ca/en/products/detail/vishay-semiconductor-opto-division/TDCR1060M/4074711) 7-segment display
    - Using 162 ohm resisistors each segment should draw 5.5mA
    - Total current draw of up to 8*5.5=44mA
    - Only one digit will ever be on at one time
-   Seven segment driver [SN74LS47DR](https://www.digikey.ca/en/products/detail/texas-instruments/SN74LS47DR/7219521)
    - nBI should be held high
    - nRBI should be held high
    - LT should be held hight
-   8:1 Decoder/Mux [SN74LV4051APWR](https://www.digikey.ca/en/products/detail/texas-instruments/SN74LV4051APWR/374749)
    - INH should be held low
    - Using decoder as current sink bad idea, so now added nMOS
-   The 4 character display has 7 lines for the segments which will be connected to the seven segment driver. Along with 6 more lines for controlling decimal places and center colon, these lines will be controlled with the MUX

### Buzzer Beeper and Dramatic LEDs Module
-   Using 3V magnetic buzzer [WT-0904T](https://www.digikey.ca/en/products/detail/soberton-inc/WT-0904T/16384510)
-   Attach to ADC pin through npn transistor [MMBT3904-TP](https://www.digikey.ca/en/products/detail/mcc-micro-commercial-components/MMBT3904-TP/717280) (if I feel like it (I did))

### Fake Batteries Module
-   Screw terminal on side of board that connect to leads of battery case.
-   High resistance voltage divider to keep current draw in miliamp range for maximum use of batteries
-   No voltage divider voltage < 3V. Connected to ADC1 for measurment 

### Configuration Jumpers (no pins left :disappointed:)
-   Any remaining GPIO pins can be connected to jumper switches to allow for 

### Expansion Interface
-   Three wire expansion interface that can be used to for another modules board or external display
-   Three screw terminal will be used 

### Power Regulation Specs
-   Device will be powered by 3 AA batteries providing nominal voltage of 4.5V
-   3V3 Regulator [LDL1117S33R](https://www.digikey.ca/en/products/detail/stmicroelectronics/LDL1117S33R/7102071) used for all components as 3V3 is good for logic and power
-   Reverse polarity protection diode [RB161MM-20TR](https://www.digikey.ca/en/products/detail/rohm-semiconductor/RB161MM-20TR/5001867)
-   Indicator LED that power is on working
-   Can be powered via usb or battery, controlled using power switch

### LED Controller
-   Using the [TLC59401PWPR](https://www.digikey.ca/en/products/detail/texas-instruments/TLC59401PWPR/2197024)
-   The RGB LEDs for each module to indicate disarmed status (3*3), the strikes display LEDs (3), and the random dramatic LEDs (up to 2) will all be connected to the driver. Another RGB next to timer for armed or disarmed entirely (only R and G will be connected).
-   Output current max can be controlled using Riref resistor and dot correction
-   For Red strikes LED and red in RGB Vf=2V, use a resistor divider to produce this voltage level. Use a 4.7k and 3k to produce 2V from 3.3V supply.
-   The G and B lights of the RGB can use dirrect 3.3V power
-   Current max of device will be set to 20mA, for red strikes LED to operate at recommended. $I_{max}=\frac{V_{IREF}}{R_{IREF}}*31.5$. Therefore $R_{IREF}=4.7k\Omega$. Using 4.7k produced limmit of 8.3mA.
-   Dot correction will be used to limmit RGB to 5mA. $I_{OUTn}=I_{max}*\frac{DC_n}{63}$ where $DC_n=0\ to\ 63$. This can be used if extra current limmiting is required
-   Extra, dramatic LEDs will be wired the same as strike indicator lights

### Wires/Buttons for LED Matrix Control
-   Use the same 8:1 decoder [SN74LV4051APWR](https://www.digikey.ca/en/products/detail/texas-instruments/SN74LV4051APWR/374749) as used for 7-segment to strobe through the 6 wires and two of the buttons for the maxtrix module
-   Use a 1:2 mux to strobe through two remaining buttons in the matrix module [SN74CBTLV3257PWR](https://www.digikey.ca/en/products/detail/texas-instruments/SN74CBTLV3257PWR/378121)
-   All buttons/wires are pulled up, connecting pulls them to ground

### Microprocessor Specs
-   Figure out what programming pins are needed
-   Planning on using the [STLINK-V3MINIE](https://www.digikey.at/en/products/detail/stmicroelectronics/STLINK-V3MINIE/16284301?srsltid=AfmBOopIx4ocnLGSitlX52VvPF4tIXacUyRYL3eHyHwXfcPgu7cQNPwkt0E&gQT=2) debugger/programmer
-   Boot mode selector switch. Pull Boot0 pin high for I2C/UART/USB programming, or pull low for run mode (SWD can overide run and program)
    - We want to pretty much always be in run mode so weak pull down to ground, if I don't want to add the switch.
-   External High frequency oscillator being used
    - Crystal [ABLS-16.000MHZ-B2-T](https://www.digikey.ca/en/products/detail/abracon-llc/ABLS-16-000MHZ-B2-T/675266?s=N4IgTCBcDaIIYCMA2BnAtARgGwDoAMBAtgBYBeaCYaALiALoC%2BQA)
    - Load Capacitance is $C_{L}=18pF$ and stray board Capacitance is in the range of 2-10pF
    - External load capacitors are calculated by $C_{load}=2*(C_{L}-C_{stray})=24pF$
    - External resistor is calculated to be very small, therefor omitted

-   See CubeIDE for specifications on connectivity

### Total Current Draw 
-   LED Controller (Red button led, module diffused status LEDs, strikes LEDS)
    - Each LED has current max of 8.3mA
    - Max current draw **140mA** (with all leds on)
-   Matrix LEDS and Controllers
    - Each LED has current max of 3.2mA
    - With all LEDS on max current draw is 144*3.2mA=**460mA**
-   Seven Segment Display
    - Using resistor based current limmiting each LED is limmited to 5.5mA
    - Only 8LEDs could be on at one time, as controller strobes. Therefore max current draw is **44mA**
- Buzzer
    - Could run up to **80mA**
-   Wires
    - If all wires are connected they burn 1mA
-   Microcontroller
    - Micro controller runs up to 74uA/MHz
    - With 16MHz, total operating current draw is **1.2mA**

-   Total Current draw = **725.2mA**