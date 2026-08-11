module arx_permutation_core #(
  parameter int ROUNDS=12
)(
  input logic clk, input logic rst_n,
  input logic in_valid, output logic in_ready, input logic [127:0] in_state,
  output logic out_valid, input logic out_ready, output logic [127:0] out_state
);
  logic [31:0] a,b,c,d; logic [$clog2(ROUNDS+1)-1:0] round_ctr; logic busy;
  function automatic [31:0] rol(input [31:0] x,input int n); rol=(x<<n)|(x>>(32-n)); endfunction
  logic [31:0] na,nb,nc,nd,t0,t1,t2,t3;
  always_comb begin
    t0=a+b; t3=rol(d^t0,16); t2=c+t3; t1=rol(b^t2,12);
    na=t0+t1; nd=rol(t3^na,8); nc=t2+nd; nb=rol(t1^nc,7);
    in_ready=!busy && !out_valid;
    out_state={d,c,b,a};
  end
  always_ff @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin a<=0;b<=0;c<=0;d<=0;round_ctr<=0;busy<=0;out_valid<=0; end
    else begin
      if(out_valid && out_ready) out_valid<=0;
      if(in_valid && in_ready) begin
        {d,c,b,a}<=in_state; round_ctr<=0; busy<=1;
      end else if(busy) begin
        a<=na;b<=nb;c<=nc;d<=nd;
        if(round_ctr==ROUNDS-1) begin busy<=0;out_valid<=1; end
        else round_ctr<=round_ctr+1'b1;
      end
    end
  end
endmodule
