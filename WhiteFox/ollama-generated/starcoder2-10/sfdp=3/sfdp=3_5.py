
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_) -> Tensor:
        v1  = torch.matmul(query_,  # type: ignore
                key_.transpose(-2, -1))  # type: ignore
        scale_factor   = self._scale_factor(v1)
        scaled_qk     = v1 * scale_factor  # type: ignore
        softmax_qk    = torch.nn.functional.softmax(scaled_qk, dim=-1)  # type: ignore
        dropout_qk    = torch.nn.functional.dropout(softmax_qk, p=0.35492677879777633)  # type: ignore
        output        = dropout_qk.matmul(value_)  # type: ignore
        return v1


# Initializing the model
m  = Model()
# Inputs to the model
__query___  = torch.randn(2508, 643)
__key___    = torch.randn(2508, 795)
__value___  = torch.randn(2508, 1024)


# Output of the model
__output___ = m(__query__, __key__, __value__)