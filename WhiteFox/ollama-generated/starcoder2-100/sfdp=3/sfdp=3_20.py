
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        scale_factor = 0.52497816
        dropout_p = 0.3
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 * scale_factor
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) 
        return v4.matmul(value)


# Initializing the model
m  = Model()


# Inputs to the model
__query  = torch.randn(56, 128)
__key  = torch.randn(56, 128)
__value  = torch.randn(56, 4096)
__output__  = m(__query, __key, __value)

