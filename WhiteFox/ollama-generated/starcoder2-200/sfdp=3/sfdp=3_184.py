

class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads  = num_heads 
        self.scale  = torch.Tensor([1]) / float(self.num_heads ** -0.5)

    def forward(self, query, key, value):
      qk  = torch.matmul(query, key.transpose(-2, -1))
      scaled_qk  = qk * self.scale
      softmax_qk  = scaled_qk.softmax(dim=-1)
      dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.1, inplace=False)
      output  = dropout_qk .matmul(value) 
      return output


# Initializing the model
m  = Model() 

# Inputs to the model
query  = torch.randn(32, 48, 56, 56).to('cuda')
key   = <KEY>(32, 48, 56, 56).to('cuda')
value   =  torch.randn(32, 48, 1, 1)


