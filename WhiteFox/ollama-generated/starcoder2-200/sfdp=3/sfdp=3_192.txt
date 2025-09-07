

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Parameter(torch.randn(1024, 768)) # Generate a random 1024 x 768 tensor as the query
        self.k = torch.nn.Parameter(torch.randn(30528, 768)) # Generate a random 30528 x 768 tensor as the key
        self.v = torch.nn.Parameter(torch.randn(30528, 1024)) # Generate a random 30528 x 1024 tensor as the value

        self.scale_factor = 1. / math.sqrt(768)
        self.dropout_p = 0

    def forward(self, input):
        
        # qk  = query @ key.t()
        qk = torch.matmul(self.q, self.k.transpose(-2, -1))
        scaled_qk = qk * self.scale_factor

        # softmax_qk = F.softmax(scaled_qk, dim=-1)
        softmax_qk = scaled_qk.softmax(dim=-1)
        
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk @ self.v

        return output

# Initializing the model
m  = Model()


# Inputs to the model
input = torch.randn(256, 30528) # Generate a random input tensor with shape 256 x 30528 for the input to the model m

__output__  = m(input)