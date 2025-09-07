

import torch 
from torch import nn 

class model(nn.Module): 
    def __init__(self): 
        super().__init__()
        self.model = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=(100), padding=(49))

    def forward(self, x): 
    	return self.model(x)

m  = model() 

