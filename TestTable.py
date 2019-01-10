import Table

if __name__ == "__main__":

    mt = Table.Table()
    mt.set_fontcolor(97)
    mt.set_bordercolor(93)
    mt.set_align("center")
    mt.addheader( ["name","gender","age","birthday","nation"] )
    mt.addrow(  ["opmdmlwk","male","32","1090-23-90","dhand"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81","11222222"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81",""] )
    # mt.printtable()

    #
    mt2 = Table.Table()
    mt2.set_fontcolor(98)
    mt2.set_bordercolor(94)
    mt2.set_align("left")
    mt2.addrow( ["This ","a","test","table","which","doesn't","has","a","header"] )
    mt2.printtable()

    #read from text
    mt3 = Table.Table()
    mt3.set_align("left")
    mt3.add_fromtext("textsample.txt",spstr = " ")
    mt3.printtable()


    #use custom split characters
    mt4 = Table.Table()
    mt4.set_align("left")
    mt4.add_fromtext("sampletexttable2.txt",spstr = "\t")
    # mt4.p_list()
    mt4.printtable()

    mt5 = Table.Table()


    mt5.wrap_text("Test string!")
#     mt5.wrap_text (
# """
# module decode_one_symbol_core_symbol_table_rsci_1_symbol_table_rsc_wait_dp (
# clk, rst, symbol_table_rsci_dout_d, symbol_table_rsci_dout_d_mxwt, symbol_table_rsci_biwt,
# symbol_table_rsci_bdwt
# );
# input clk;
# input rst;
# input [7:0] symbol_table_rsci_dout_d;
# output [7:0] symbol_table_rsci_dout_d_mxwt;
# input symbol_table_rsci_biwt;
# input symbol_table_rsci_bdwt;
#
# // Interconnect Declarations
# reg symbol_table_rsci_bcwt;
# reg [7:0] symbol_table_rsci_dout_d_bfwt;
# // Interconnect Declarations for Component Instantiations
# assign symbol_table_rsci_dout_d_mxwt = MUX_v_8_2_2(symbol_table_rsci_dout_d, symbol_table_rsci_dout_d_bfwt,
# symbol_table_rsci_bcwt);
# always @(posedge clk) begin
# if ( ~ rst ) begin
# symbol_table_rsci_bcwt <= 1'b0;
# end
# else begin
# symbol_table_rsci_bcwt <= ~((~(symbol_table_rsci_bcwt | symbol_table_rsci_biwt))
# | symbol_table_rsci_bdwt);
# end
# end
# always @(posedge clk) begin
# if ( ~ rst ) begin
# symbol_table_rsci_dout_d_bfwt <= 8'b00000000;
# end
# else if ( ~ symbol_table_rsci_bcwt ) begin
# symbol_table_rsci_dout_d_bfwt <= symbol_table_rsci_dout_d_mxwt;
# end
# end
# """)
