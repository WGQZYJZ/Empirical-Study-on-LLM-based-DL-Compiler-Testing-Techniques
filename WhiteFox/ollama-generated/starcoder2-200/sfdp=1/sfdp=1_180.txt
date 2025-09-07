
class Model(torch.nn.Module):
    def __init__(self, query):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.Tensor([0]))

    def forward(self, x1):
      qk = torch.matmul(query, key)
      scaled_qk = qk / scale
      softmax_qk = scaled_qk.softmax(-2)
      dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
      output  = dropout_qk @ value
      return output

# Initializing the model and setting the query tensor input
m  = Model(query1)

 # Inputs to the model (assuming all the inputs have been pre-defined)
x1  = torch.randn(1, 640)
__output__  = m(x1) 
