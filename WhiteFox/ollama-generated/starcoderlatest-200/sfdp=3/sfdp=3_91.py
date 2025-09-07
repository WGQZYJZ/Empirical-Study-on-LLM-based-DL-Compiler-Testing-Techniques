
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(1024, 1024)
 
    def forward(self, q1, k1, v1):
        query_tensor = q1.matmul(k1.transpose(-2, -1))
        softmax_qk_tensor = query_tensor.softmax(dim=-1)
        dropout_qk_tensor  = torch.nn.functional.dropout(softmax_qk_tensor, p=0.4)
        output_tensor    = torch.matmul(dropout_qk_tensor, v1)
        return output_tensor
 

# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(512, 3, 64, 64)
k1  = torch.randn(512, 3, 64, 64)
v1  = torch.randn(512, 3, 64, 64)
