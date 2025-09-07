
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.randn([1,]))
        self.query  = torch.nn.Parameter(torch.randn([50,  50]))
        self.key    = torch.nn.Parameter(torch.randn([50,  32]))
 
    def forward(self):
        qk  = torch.matmul(self.query, self.key.transpose(-2, -1))
        skq  = qk.mul(scale_factor)
        smqk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(smqk, p=p)
        output = softmax_qk.matmul(self.value)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
  query   = torch.randn([50,    1])
key  = torch.randn([32,   50])
value = torch.randn([32,   64])
dropout_p  = 0.7
scale_factor  = 0.8

 # Outputs from the model
  model(torch.randn([1,  3, 64, 64]))
