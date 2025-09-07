
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.transformer = torch.nn.Transformer()
 
    def forward(self, input1):
        scaled_dot_product  = ...  # Compute the scaled dot product attention here 
        # Add any other operations required by the Transformer model
        output  = ... # Perform the necessary computations to generate the output
        return output

# Initializing the model with an arbitrary number of tokens and embeddings
m1, m2 = Model(), Model()

 # Create input tensors of shape (batch_size, num_tokens) for the models m1 and m2 
x1 = torch.randn(307489, 512)
x2 = torch.randn(614857, 512)

 # Run the forward pass of model m1 with input x1
y1_m1  = m1(x1)
 
 # Run the forward pass of model m2 with input x2
y2_m2  = m2(x2)
 
 # Obtain a batch of 307489 tokens from y1_m1 and compare it to a batch of 614857 
 # tokens from y2_m2. The inputs should be different!
