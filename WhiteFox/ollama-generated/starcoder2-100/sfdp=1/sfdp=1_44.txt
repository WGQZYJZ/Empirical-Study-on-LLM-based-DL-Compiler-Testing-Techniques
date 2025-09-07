
class SelfAttention(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, scale_factor: int = 1) -> None:
        super().__init__()
        self.query = query
        self.key   = key
        self.value = value
        self.scale_factor = scale_factor
 
    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))  # Compute the dot product of the query and key tensors 
        scaled_qk  = qk / self.scale_factor   # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)  # Apply dropout to the softmax output
        output     = dropout_qk.matmul(self.value)  # Compute the dot product of the dropout output and the value tensor 
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.selfatt1 = SelfAttention()
        self.selfatt2 = SelfAttention()
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        v0  = x1 + self.selfatt1() # Add the output of a new self-attention layer to the input tensor x1 
        v1  = self.selfatt2(v0).relu() # Apply ReLU to the output of another self attention layer with input data x0
        return v1


# Initializing the model and its inputs:
m  = Model()
 
x1 = torch.randn(5, 4)
x2 = torch.randn(3, 8, 6, 7)
__output__  = m(x1, x2)

