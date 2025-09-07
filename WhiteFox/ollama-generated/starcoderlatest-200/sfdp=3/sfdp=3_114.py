
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 64, 1, stride=1, padding=0)
        self.key   = torch.nn.Conv2d(3, 64, 1, stride=1, padding=0)
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(16, 3, 1024, 768)
key   = torch.randn(16, 3, 1024, 768)
