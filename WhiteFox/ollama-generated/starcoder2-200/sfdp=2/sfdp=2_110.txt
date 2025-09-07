
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout()
        self.scalefactor  = 0.5
        self.invscalefact = 1/self.scalefactor
        self.softmax  = torch.nn.Softmax(dim=-2)
 
    def forward(self, query, key, value):
       v1=query*key.transpose(-2,-1)
       v2=v1/self.invscalefact
       v3=self.softmax(v2)
       v4=self.dropout(v3)
       v5=v4.matmul(value)
       return  v5

# Initializing the model<|end_of_model|>
m = Model()

 # Inputs to the model<|end_of_inputs|> 
 query = torch.randn(2, 8, 1024)
 key = torch.randn(2, 8, 768)
 value = torch.randn(2, 8, 512)

 # Output from the model<|end_of_output|>
 __output__=m(query,key,value)
