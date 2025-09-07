
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.randn(32, 768) # query tensor
        self.key = torch.randn(32, 768) # key tensor 
        self.value = torch.randn(32, 1024) # value tensor
 
    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))
        scale_factor = float(np.random.uniform(87600, 95895).round()) / 93453 # random scaling factor in range (0.87600-0.95895)
        scaled_qk = qk/scale_factor
 
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # random dropout parameter
        output  = dropout_qk @ self.value # dot product of the dropout output and value tensor
        return output

# Initializing the model
m = Model()


Inputs to the model:<|input_names|>
x1 = torch.randn(32, 768)
x2 = torch.randn(32, 768)
x3 = torch.randn(32, 1024)
x4 = m()

