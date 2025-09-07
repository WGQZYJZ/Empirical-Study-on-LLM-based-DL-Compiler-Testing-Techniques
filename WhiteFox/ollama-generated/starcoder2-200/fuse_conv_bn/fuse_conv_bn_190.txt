
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv1d(2, 3, kernel_size=5) # Conv 1D: 1d -> 3d 
        self.bn   = torch.nn.BatchNorm1d(3)               # Batch Norm1d: 1d -> 3d 

    def forward(self, x):
        conv1d =  torch.nn.functional.conv1d(x, self.conv.weight)    
        v2     = torch.nn.functional.batch_norm(conv1d) 
        return v2

m = Model()

 # Inputs to the model
__input__ = torch.randn(3000, 18, 512)  # The input must contain more than one batch dimension (X)

 