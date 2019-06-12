
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input('../examples/gray.jpg', name='input'),

    #block
    to_ConvConvRelu( name='conv2d_1,2', s_filer='', n_filer=(8,8), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=32, depth=32),
    to_Conv('conv2d_3', s_filer='I/2', n_filer=16, offset="(0.8,0,0)", to="(conv2d_1,2-east)", width=3, height=32, depth=32),
    to_Conv('conv2d_4', s_filer='I/4', n_filer=16, offset="(1.5,0,0)", to="(conv2d_3-east)", width=3, height=25, depth=25),
    to_Conv('conv2d_5', s_filer='I/4', n_filer=32, offset="(1.5,0,0)", to="(conv2d_4-east)", width=4, height=25, depth=25),
    to_Conv('conv2d_6', s_filer='I/8', n_filer=32, offset="(1.5,0,0)", to="(conv2d_5-east)", width=4, height=16, depth=16),
    to_Conv('conv2d_7', s_filer='I/8', n_filer=64, offset="(1.5,0,0)", to="(conv2d_6-east)", width=5, height=16, depth=16),
    to_Conv('conv2d_8', s_filer='I/16', n_filer=64, offset="(1.5,0,0)", to="(conv2d_7-east)", width=5, height=8, depth=8),
    to_Conv('conv2d_9', s_filer='I/16', n_filer=128, offset="(1.5,0,0)", to="(conv2d_8-east)", width=6, height=8, depth=8),
    to_Conv('up_sampling2d_1', s_filer='I/8', n_filer=128, offset="(1.5,0,0)", to="(conv2d_9-east)", width=6, height=16, depth=16), # upsampling
    to_Conv('conv2d_10', s_filer='I/8', n_filer=64, offset="(1.5,0,0)", to="(up_sampling2d_1-east)", width=5, height=16, depth=16),
    to_Conv('up_sampling2d_2', s_filer='I/4', n_filer=64, offset="(1.5,0,0)", to="(conv2d_10-east)", width=5, height=25, depth=25), # upsampling2
    to_Conv('conv2d_11', s_filer='I/4', n_filer=32, offset="(1.5,0,0)", to="(up_sampling2d_2-east)", width=4, height=25, depth=25),
    to_Conv('up_sampling2d_3', s_filer='I/2', n_filer=32, offset="(1.5,0,0)", to="(conv2d_11-east)", width=4, height=32, depth=32), # upsampling3
    to_Conv('conv2d_12', s_filer='I/2', n_filer=16, offset="(1.5,0,0)", to="(up_sampling2d_3-east)", width=3, height=32, depth=32),
    to_Conv('up_sampling2d_4', s_filer='I', n_filer=16, offset="(1.5,0,0)", to="(conv2d_12-east)", width=3, height=40, depth=40), # upsampling4
    #to_Conv('conv2d_13', s_filer='I', n_filer=2, offset="(2,0,0)", to="(up_sampling2d_4-east)", width=1, height=40, depth=40),
    to_ConvSoftMax(name='tanh', s_filer='I', offset="(2,0,0)", to="(up_sampling2d_4-east)", width=1, height=40, depth=40, caption="2"),
    to_connection("conv2d_3", "conv2d_4"),
    to_connection("conv2d_4", "conv2d_5"),
    to_connection("conv2d_5", "conv2d_6"),
    to_connection("conv2d_6", "conv2d_7"),
    to_connection("conv2d_7", "conv2d_8"),
    to_connection("conv2d_8", "conv2d_9"),
    to_connection("conv2d_9", "up_sampling2d_1"),
    to_connection("up_sampling2d_1", "conv2d_10"),
    to_connection("conv2d_10", "up_sampling2d_2"),
    to_connection("up_sampling2d_2", "conv2d_11"),
    to_connection("conv2d_11", "up_sampling2d_3"),
    to_connection("up_sampling2d_3", "conv2d_12"),
    to_connection("conv2d_12", "up_sampling2d_4"),
    to_connection("up_sampling2d_4", "tanh"),
    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
