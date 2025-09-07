
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 32)
        self.norm1  = torch.nn.LayerNorm(32)
        self.dropout1 = torch.nn.Dropout(0.5)
        self.activation = torch.nn.ReLU()
 
        self.linear2 = torch.nn.Linear(32, 8)
        self.norm2  = torch.nn.LayerNorm(32)
 
    def forward(self, query): 
        key1 = self.dropout1(self.activation(query))
        value1 = self.norm1(key1)
 
        key2 = self.norm2(value1)
        value2 = self.linear2(key2)
        output  = torch.matmul(self.dropout1(value2), query)
        return output


# Initializing the model
m  = Model()

# Inputs to the model
query1 = torch.randn(3, 8, 64, 64)
__output__   = m(query1)

# Output of the model on query1 with dropout_p=0.5 and inv_scale_factor=2
torch.Size([3, 8, 79, 79])