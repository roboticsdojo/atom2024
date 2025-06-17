/* *************************************************************
   Encoder driver function definitions - by James Nugen
   ************************************************************ */
   
   
#ifdef ARDUINO_ENC_COUNTER
  //below can be changed, but should be Interrupt pins (Confirm the interrupt pins in the board you are using)
  //otherwise additional changes in the code are required
  #define LEFT_ENC_PIN_A PD2  //pin 2
  #define LEFT_ENC_PIN_B PD3  //pin 3
  
  //below can be changed, but should be PORTC pins
  #define RIGHT_ENC_PIN_A 21 //pin 21
  #define RIGHT_ENC_PIN_B 20 //pin 20 
#endif
   
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();