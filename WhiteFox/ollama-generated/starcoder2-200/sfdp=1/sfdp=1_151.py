
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.Tensor([0.3]))
 
    def forward(self, query, key, value):
        scaled_qk  = (torch.matmul(query, key.transpose(-2, -1)) * inv_scale).div_(self.scale)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5)
 
        output  = dropout_qk @ value # Compute the dot product of the dropout output and a value tensor
        return output

# Initializing the model
model  = Model()


# Inputs to the model
query1  = torch.rand(4, 8, 32) * 0.5
key1  = torch.rand(4, 6, 32).transpose(-2, -1) * 0.7
value1  = torch.rand(4, 9, 32) + 0.5
 
# Outputs of the model
__output___1  = model(query1, key1, value1)


# Inputs to the model
query2  = torch.rand(876, 32).div_(inv_scale * self.scale) - 10.5
key2  = torch.rand(4, 9, 32) + 0.7
value2  = torch.rand(4, 8, 32) / 6
 
# Outputs of the model
__output___2  = model(query2, key2, value2)

