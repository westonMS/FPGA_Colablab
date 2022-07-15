module top(
    input logic[15:0] sw,
    input wire logic btnu, btnd, btnl, btnr,
    output logic[15:0] led
);

always_comb begin
    if(btnl) begin
        led[15:8] = 0;
        led[7:0] = sw[15:8] ^ sw[7:0];
        end
    else if(btnr) begin
        led[15:1] = 0;
        if(sw == 16'hFFFF)
            led[0] = 1'b1;
        else
            led[0] = 1'b0; 
        end
    else if(btnd)
        led = sw << 3;
    else if(btnu)
        led = 0;
    else
        led = sw;
end

endmodule
