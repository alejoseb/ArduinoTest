target remote | openocd -f interface/stlink-v2-1.cfg -f target/stm32f1x.cfg -f gdb-pipe.cfg
monitor halt
monitor gdb_sync
stepi
