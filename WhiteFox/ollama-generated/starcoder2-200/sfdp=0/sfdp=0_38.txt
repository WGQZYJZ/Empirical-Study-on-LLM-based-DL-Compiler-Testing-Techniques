
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.embedder = torch.nn.Embedding(2048, 768)
 
    def forward(self, input1):
        query = input1[0]
        key = input1[1]
        inv_scale = float(key.shape[-1]) ** -0.5
        
        scaled_dot_product = torch.matmul(query, key.transpose(-2,-1))/inv_scale

        attention_weights =  scaled_dot_product.softmax(dim=-1)

        value = input1[3]
        output = attention_weights @ value
        return output

# Initializing the model and generating inputs to it
m = Model()
input1 = [torch.randint(0,2048,(768,)) for _ in range(5)]
input2  = torch.randint(0,2048,(768,))

 # Generating an input to the model: keys and query tensors of different size and shapes.
input1[3] = m.embedder.weight
