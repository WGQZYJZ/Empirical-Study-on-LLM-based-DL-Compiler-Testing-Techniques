
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = v1 * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = dropout_p * self.softmax(softmax_qk)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query, key, value  = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 64, 64), torch.randn(1, 8, 64, 64)
__output__  = m(query, key, value)

