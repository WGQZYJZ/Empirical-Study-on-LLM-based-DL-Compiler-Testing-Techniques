
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 8)
        self.key = torch.nn.Linear(32, 16)
        self.scale_factor = torch.nn.Parameter(torch.Tensor([[0.5]]).to('cuda:0'), requires_grad=True)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, self.key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()


