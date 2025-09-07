
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.rand(1) * 0.05
 
        self.query = torch.nn.Parameter(torch.randn(2, 8))
 
    def forward(self, key):
        value  = torch.randn(key.shape[0], key.shape[-1])
        qk     = torch.matmul(self.query, key) 
        scaled_qk  = qk / self.scale
        softmax_qk  = scaled_qk.softmax(-1)
 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25)
        output    = dropout_qk * value
        return output


# Initializing the model with different parameters (in this case: the query is not randomly generated in the forward method).
m  = Model()
 
# Input tensors for the model 
x1 = torch.randn(3, 8) # The shape of tensor x2 is (3, 5, 64), and its shape is (3, 7, 30). Also note that the shapes are different from the previous model inputs.
 
 # Initializing the optimizer with a random learning rate
optimizer = torch.optim.Adam(m.parameters(), lr=torch.rand(1) * 5)
 

