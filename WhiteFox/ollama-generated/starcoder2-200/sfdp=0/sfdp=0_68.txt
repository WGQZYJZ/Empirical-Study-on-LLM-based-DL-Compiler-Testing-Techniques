
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.att = torch.nn.MultiheadAttention(32, 16)
 
    def forward(self, query, key, value):
        
        output = self.att(query, key, value)[0]

        return output


# Initializing the model
m = Model()
 
__output__  = m(torch.randn(5, 32), torch.randn(16*10, 32))
 
