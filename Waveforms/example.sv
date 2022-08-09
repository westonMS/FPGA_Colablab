module example(
    input logic inc,
    input logic clk,
    input logic reset,
    output logic[15:0] count
)

always_ff(@posedge clk)
    if(reset)
        count <= 0;
    else if(inc)
        count <= count + 1;

endmodule