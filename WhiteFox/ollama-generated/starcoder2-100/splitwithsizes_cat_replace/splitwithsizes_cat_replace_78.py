
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
       # Split input tensor along the channel dimension by chunks of size 4 (the number of channels is 8), and concatenate them back into a single tensor along the same dimension
        v1 = torch.split(x1, 4, dim=1)
        v2 = [torch.cat([v1[i][j] for j in range(len(v1))], 0).unsqueeze(-3) for i in range(len(v1))] 
        return self._model(self.conv, v2)
    
    def _model(self, model_conv, model):
       # ... the model

# Initializing the model
m = Model()


# Inputs to the model 
x1 = torch.randn(8, 3, 40, 40)
__output__  = m(x1)
