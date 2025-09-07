
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) + self.__other__ 
        return torch.relu(v1)

 # Initializing the model and passing `other` as a keyword argument
m  = Model()
m_output = m(x1, other=other)

