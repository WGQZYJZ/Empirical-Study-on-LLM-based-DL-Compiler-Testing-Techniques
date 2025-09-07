

class Model(torch.nn.Module):
    def __init__(self, num_tokens, emb_dims=512, hiddens=[2048]):
        super().__init__()
 
        self._token_embedding = torch.nn.Embedding(num_tokens, emb_dims)  # Generate embedding matrices for the tokens of the model. The number of tokens is equal to the total number of distinct words in the corpus and each word is represented by a vector with size 512.
        self._dropout = torch.nn.Dropout(0.3)
 
        def build_encoder():
            return nn.Sequential(
                nn.Conv1d(),
                nn.ReLU()
            )
 
        self._encoder = nn.Sequential(
            *([build_encoder()] + [build_encoder()]) for _ in range(2))
        self._mlp = MLP(num_hidden=hiddens)
 
    def forward(self, x):
        bs = x.size(0)  # Get the batch size of the input
        x1  = self._token_embedding(x).permute(0, 2, 1).contiguous()
        x2  = self._dropout(x1) 
        res  = self._encoder(x1.permute(0, 2, 1)) + x2
        x3 = torch.flatten(res, start_dim=1)  
        v4  = self._mlp(x3)
        return v4


# Initializing the model and generating an input tensor to the model:

 #Model initialization
    model = Model()
 
	#Input tensor
    input_tensor = torch.randint(0,9,(256))
 
 #Call the forward function with different inputs:
    output  = model(input_tensor)
