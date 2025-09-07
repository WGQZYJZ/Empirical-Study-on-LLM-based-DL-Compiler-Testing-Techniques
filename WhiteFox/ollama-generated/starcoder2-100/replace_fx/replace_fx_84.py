
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t3 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor with probability of 0.5
         t4 = torch.rand_like(t3, out=None).clone() # Clone and fill up a tensor with random numbers with the same size as t3

        # Replace the original nodes for these functions with its replacements
        replacement_fn = lowmem_dropout if fallback_random else 0

        self.replace_fx(
            t3, torch.nn.functional.lowmem_dropout, 
            replacement_fn)
        
        self.replace_fx(t4, torch.rand_like, replacement_fn)
        
        return t2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1000, 375)
 
 