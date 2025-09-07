
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.randn(32, 64)
        self.key = torch.randn(32, 1024)
        self.value = torch.randn(32, 1024)
 
        self.scale_factor = 5
 
 
    def forward(self):
        self.qk = torch.matmul(self.query,
                               self.key.transpose(-2,-1))
        self.scaled_qk = self.qk / self.scale_factor
        self.softmax_qk = scaled_qk.softmax(dim=-1)
 
        self.dropout_qk = torch.nn.functional.dropout(
            self.softmax_qk, p=0.8
        )
        self.output = dropout_qk @ self.value
        return self.output


# Initializing the model
m  = Model()
 
# Inputs to the model
query  = torch.randn(16, 32)
key  = torch.randn(16, 512)
value  = torch.randn(16, 512)
 
__output__  = m()

