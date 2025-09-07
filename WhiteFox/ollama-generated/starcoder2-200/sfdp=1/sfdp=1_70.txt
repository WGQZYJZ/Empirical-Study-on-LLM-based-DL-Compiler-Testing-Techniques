
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inv_scale = torch.nn.Parameter(
            100, requires_grad=True)
        self.dropout = torch.nn.Dropout(p=.5)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor): 
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale.item())
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk) 
        output  = dropout_qk.matmul(value)
 
        return output


# Initializing the model
m = Model()

 # Inputs to the model
qk = torch.randn(4, 3072) + 10
key = torch.randn(4, 64, 8, 8).reshape(-1, 5 * 5 * 8) / np.sqrt(
    5 * 5 * 8)  # Scale the matrix by a constant to satisfy an equation in the first line of this model
value = torch.randn(4, 3072 + 64*8, 1, 1).reshape(-1, 3072 + 64*8) / np.sqrt(
    5 * 5 * 8)
