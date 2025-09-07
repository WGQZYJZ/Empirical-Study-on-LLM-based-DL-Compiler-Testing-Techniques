
class MyModel(torch.nn.Module):
    def __init__(self, inputSize=512):
        super().__init__()
        self.inputSize = 512
        self.outputSize = 80
        
        # Initialize the embedding layers.
        self.embedding = nn.Embedding(self.inputSize + 1, 3)
        self.embedding_weights = torch.randn(768, self.inputSize)
        self.linear = nn.Linear(3 * inputSize, 504)

        # Initialize the weights of embedding layer with random values and biases to zero.
        self.embedding.weight.data.copy_(self.embedding_weights)
        self.embedding.weight.requires_grad = False
        self.linear.bias.data.fill_(0)

        # Initialize the bias of embedding layer to zero.
        self.linear2 = nn.Linear(3*inputSize, 517)

    def forward(self, x):
        
        ql = self.embedding(x)
        kq_mul = torch.bmm(ql, ql.permute(0,2,1)) # batch_size, len(seq), len(seq)
    
        attn_weights = kq_mul.softmax(-1)

        attn_weights = F.dropout(attn_weights, p=0.5, training=self._training, inplace=False)
    
        output  = torch.bmm(attn_weights, ql) # batchsize, len(seq), embeding_dim
        out = self.linear(output)
        return out

# Initializing the model
m1 = MyModel()


# Inputs to the model
x1 = torch.randint(0, m1.inputSize - 1,(32,))
__output__  = m1(x1)


