
class Model(torch.nn.Module):
    def __init__(self, min_value=-25, max_value=10893.746):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(in_channels=3, out_channels=8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    
    def forward(self, x):
       v1 = self.conv(x)
       v2 = torch.clamp_min(v1, min=-0.5767988443374634) # This value can be different from the original one in your solution; you may need to find a good random seed (use `torch.manual_seed()`)
       v3 = torch.clamp_max(v2, max=0.15993809676170349)  # This value can be different from the original one in your solution; you may need to find a good random seed (use `torch.manual_seed()`)
       return v3

# Initializing the model
m = Model(min_value=-25, max_value=10893.746)

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)


__output__  = m(x)
 
