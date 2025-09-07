
class Model(torch.nn.Module):
    def __init__(self, k1 = torch.nn.Linear(2048,5), k2 = 36, k3= 'constant'):
        super().__init__()
        self.conv  = torch.nn.Conv2d(k1, k2 , kernel_size=(7, 7), stride=(2, 2), padding=(3, 3))
        self._initialize_weights()
 
    def forward(self): # the model without argument
        v1  = self.conv(x)
        v2  = v1 - k3

# Initializing the model