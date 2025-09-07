
class Model(torch.nn.Module):
    def __init__(self, split_sizes: int = 3):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        self.split_sizes  = [4] * (split_sizes - 1) + [4]
    
    def forward(self, x1): 
        v1  = self.conv(x1)
        splitted  = torch.split(v1, 32, dim=0)
        concatenated  = torch.cat([splitted[i] for i in range(len(split_sizes))],dim=0)

        return concatenated


# Initializing the model<|end_of_model|>
m  = Model()

 # Inputs to the model
 x1  = torch.randn(4,32,64,64)
 
 # Model's output
 