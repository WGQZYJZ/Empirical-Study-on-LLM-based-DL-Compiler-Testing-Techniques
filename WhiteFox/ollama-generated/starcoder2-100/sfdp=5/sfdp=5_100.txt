
class MyModel(torch.nn.Module):
    def __init__(self, hparams):
        super().__init__()
 
        # Initialize the linear layer with hyperparameters hparams['embed'] (the input dimension) 
        # and hparams['hidden'][0] (the output dimension) as weights. The bias is initialized to 1.
        self.linear = torch.nn.Linear(hparams["embed"], hparams["hidden"][0], bias=True)
 
        # Initialize the linear layer with hyperparameters hparams['hidden'][-1] 
        # and len(hparams['vocab']) as weights. The bias is initialized to 0.
        self.out = torch.nn.Linear(hparams['hidden'][-1], len(hparams["vocab"]), bias=True)
 
    def forward(self, input):

        # Apply the non-linear ReLU activation function to the output of linear layer: output1 = torch.relu(output0).
        # Use the hyperparameter hparams['dropout'][0] for dropout. Dropout is then applied 
        # to this layer using the torch.nn.functional.dropout function (don't forget to use 'inplace'=True).
        output1 = self.linear(input)
        output1 = torch.nn.functional.relu(output1, inplace=True)
 
        # Apply dropout: output2 is output0 after applying dropout.
        # Use the hyperparameter hparams['dropout'][1] for dropout (don't forget to use 'inplace'=True).
        output2 = torch.nn.functional.dropout(output1, p=hparams["dropout"][1], inplace=True)

        return self.out(output2)
