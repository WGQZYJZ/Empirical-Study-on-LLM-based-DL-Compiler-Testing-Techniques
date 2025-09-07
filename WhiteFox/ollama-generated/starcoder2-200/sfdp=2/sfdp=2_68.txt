
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1: torch.Tensor) -> torch.Tensor:

        key  = torch.randn(500, 4993280)
        value  = torch.randn(768, 4993280)
        scale_factor  = 0.01
        dropout_p  = 0.05
        scaled_qk  = query1 * key.transpose(-2, -1).div_(scale_factor)
        softmax_qk  = torch.nn.functional.softmax(scaled_qk, dim=-1)
        output  = dropout_qk.matmul(value)

        return output

# Initializing the model
m = Model()

# Inputs to the model
query1 = torch.randn(500, 768)
__output__  = m(query1)

