class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding = torch.nn.Embedding(20, 5) 
        self.pos_embedding   = torch.nn.Embedding(16, 5)
 
        self.attention1 = ScaledDotProductAttention()
        self.layernorm1 = torch.nn.LayerNorm(5)
        self.dropout    = torch.nn.Dropout(0.2)
 
    def forward(self, x):

        output = []
        for i in range(3):
            input_embedding  = (x * 4) ** 0.7 + \
                                (torch.randn(16).float() /
                                 sqrt(inv_scale)) 

            pos_embedding     = self.pos_embedding(
                                        torch.arange(20, device='cuda').long())
            query             = torch.nn.functional.softmax(
                                    self.token_embedding(x))
            
            # Scaled Dot Product Attention
            value              = self.attention1(
                                        (query * 4) ** 0.7 + pos_embedding, 
                                        torch.randn((20, 5), device='cuda').float() /
                                        sqrt(inv_scale))
            output.append(value)
        return self.layernorm1(output[0] + output[1])
