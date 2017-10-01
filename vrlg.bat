@echo off
iverilog -o %~n1 %1
vvp %~n1