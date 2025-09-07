
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        qk = torch.matmul(query1, key2.transpose(-2, -1))
        sk  = scale_factor * qk 
        softmax_qk = sk.softmax(dim=-1)  
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output4  = dropout_qk.matmul(value3)
        return output


# Initializing the model and specifying the input tensors for the forward function in the model to execute it. 
m1 = Model()  
q = torch.randn([8, 64], requires_grad=True).to('cuda')
k2 = torch.randn([8, 32, 64, 64]).to('cuda') # query and value have the same shape here because they are in different layers of a transformer network
v3 = torch.randn([8, 10, 64], requires_grad=True).to('cuda')

 __output__  = m(q, k2, v3)

# Questionnaire for Model Analyzer:
1. Which operators are in the pattern?
2. In which order does each operator appear?
3. What kind of inputs is used to execute the model?
4. Does the model contain operations that do not meet the requirements?
