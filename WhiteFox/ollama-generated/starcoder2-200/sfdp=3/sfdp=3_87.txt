
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(data=0.1, requires_grad=True)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, scale_factor: float, dropout_p: float):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1.mul(scale_factor)
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4.matmul(value)


# Initializing the model and setting its hyperparameters to their default values
query = torch.randn((8, 6))
key = torch.randn((20, 12, 5))
value = torch.randn((70, 32, 5))
 
m  = Model()
scale_factor  = 1e-4
dropout_p  = 0.9
 
m(query=query, key=key, value=value, scale_factor=scale_factor, dropout_p=dropout_p)
 
