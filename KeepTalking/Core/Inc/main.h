/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2025 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32l4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define ADC1_IN5_Fake_Batt_Pin GPIO_PIN_0
#define ADC1_IN5_Fake_Batt_GPIO_Port GPIOA
#define Wires_Input1_Pin GPIO_PIN_1
#define Wires_Input1_GPIO_Port GPIOA
#define Wires_Input2_Pin GPIO_PIN_2
#define Wires_Input2_GPIO_Port GPIOA
#define Wires_Input3_Pin GPIO_PIN_3
#define Wires_Input3_GPIO_Port GPIOA
#define Wires_Input4_Pin GPIO_PIN_4
#define Wires_Input4_GPIO_Port GPIOA
#define Wires_Input5_Pin GPIO_PIN_5
#define Wires_Input5_GPIO_Port GPIOA
#define Wires_Input6_Pin GPIO_PIN_6
#define Wires_Input6_GPIO_Port GPIOA
#define Red_Button_Input_Pin GPIO_PIN_7
#define Red_Button_Input_GPIO_Port GPIOA
#define Expan_Output_Pin GPIO_PIN_0
#define Expan_Output_GPIO_Port GPIOB
#define LPTM1_Out_Buzz_Pin GPIO_PIN_2
#define LPTM1_Out_Buzz_GPIO_Port GPIOB
#define LED_Out_Mode_Pin GPIO_PIN_10
#define LED_Out_Mode_GPIO_Port GPIOB
#define LED_Out_XLAT_Pin GPIO_PIN_11
#define LED_Out_XLAT_GPIO_Port GPIOB
#define Seg_7_Drv_OutputA_Pin GPIO_PIN_12
#define Seg_7_Drv_OutputA_GPIO_Port GPIOB
#define Seg_7_OutputB_Pin GPIO_PIN_13
#define Seg_7_OutputB_GPIO_Port GPIOB
#define Seg_8_OutputC_Pin GPIO_PIN_14
#define Seg_8_OutputC_GPIO_Port GPIOB
#define Seg_7_OutputD_Pin GPIO_PIN_15
#define Seg_7_OutputD_GPIO_Port GPIOB
#define LPTIM2_Out_GSCLK_Pin GPIO_PIN_8
#define LPTIM2_Out_GSCLK_GPIO_Port GPIOA
#define Matrix_SDB_Output_Pin GPIO_PIN_11
#define Matrix_SDB_Output_GPIO_Port GPIOA
#define Matrix_INTB_Input_Pin GPIO_PIN_12
#define Matrix_INTB_Input_GPIO_Port GPIOA
#define Sev_Seg_Mux_Output0_Pin GPIO_PIN_5
#define Sev_Seg_Mux_Output0_GPIO_Port GPIOB
#define Sev_Seg_Mux_Output1_Pin GPIO_PIN_6
#define Sev_Seg_Mux_Output1_GPIO_Port GPIOB
#define Sev_Seg_Mux_Output2_Pin GPIO_PIN_7
#define Sev_Seg_Mux_Output2_GPIO_Port GPIOB
#define LED_Out_Sin_Pin GPIO_PIN_8
#define LED_Out_Sin_GPIO_Port GPIOB
#define LED_Out_SCLK_Pin GPIO_PIN_9
#define LED_Out_SCLK_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
