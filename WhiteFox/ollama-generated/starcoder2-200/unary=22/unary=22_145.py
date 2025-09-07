
class Model(torch.nn.Module):
    def __init__(self, inputSize=1024, hiddenSize=512, outputSize=6):
        super().__init__()
 
        self.fc = torch.nn.Linear(inputSize, 
                                  hiddenSize) # Apply a linear transformation to the input tensor
        
        self.hiddenFC = torch.nn.Linear(hiddenSize, outputSize)
    
    def forward(self, x1):

        v1 = self.fc(x1)
        v2 = F.softmax(v1, dim=0)
        v3 = torch.tanh(v2)
        v4 = self.hiddenFC(v3)

        return v4


m  = Model()
__output__  = m(x1)

# Initializing the model