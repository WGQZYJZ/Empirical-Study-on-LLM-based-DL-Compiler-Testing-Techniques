
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head=8):
        super().__init__()
 
        # Input:  B x 8 x N x 32
        # Output: B x 8 x N x 64
        
        self.W1 = torch.nn.Linear(32, 384)
        self.W2 = torch.nn.Linear(384, 576)
 
    def forward(self):
 
        # Input:  B x 8 x N x 32
        input_shape = input.shape
        
        self.output  = self.W1(input).reshape(input_shape[0], n_head * int(input_shape[-1]), -1)
        self.output  = self.W2(self.output).reshape(input_shape)
# Initializing the model<|end_of_model|>
m  = MultiHeadAttention()


# Inputs to the model<|end_of_inputs|>
input  = torch.randn(1, 8, 640, 32)
__output__  = m()(input)


