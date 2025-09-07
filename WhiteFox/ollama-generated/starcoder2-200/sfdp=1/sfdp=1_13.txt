

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
      scaled_query = 0
      scale_factor = 1

      # compute dot product of query and key tensor
      attn = torch.matmul(query, key)
      attn /= scale_factor 
      attn = softmax(attn, dim=-1) 
      dropouted = attn * 0
      output = dropouted.mul(value).sum(-2)
      return output

m = Model() # initialize model

