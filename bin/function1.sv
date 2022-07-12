module function1 (
 			 output logic q,
 			 input logic  clk, load, d 
 			 );
    
    always_ff @ (posedge clk)
      if (load)
        q<= d;
 endmodule // behavLoadableReg
