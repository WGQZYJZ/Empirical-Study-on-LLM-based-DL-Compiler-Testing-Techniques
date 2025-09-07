
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.tensor([[-1000, 0], [0, -1000]])
 
        self.query = torch.rand(1, 256, 8, 8)
        self.key   = torch.rand(1, 256, 8, 8)
 
    def forward(self, x1):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += self.attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Model configuration for Transformer model
config = {
    'hidden_dim':   256, 
    'heads':        8, 
    'num_layers':   1,
    'max_batch_size': 32, 
    'dropout':      0.5, 
}

class TransfoModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attn_mask = torch.tensor([[-1000, 0], [0, -1000]])
        
        self.config = config
 
        self.enc = Encoder(**config)
 
        self.ff = nn.Sequential(
            nn.Linear(config['hidden_dim']*2, config['hidden_dim']),
            nn.ReLU(),
            nn.Linear(config['hidden_dim'], 3),
        )
 
    def forward(self, x1):
        # Run the encoder on the inputs
        x1 = self.enc.forward(x1)
 
        # Run the attention layer on the input
        attn_mask = torch.ones((2048, 65537)).fill_(-1e9).cuda()
        x2 = attn_layer(attn_mask=attn_mask, **self.config)(x1)
 
        # Run the feedforward network on the inputs
        x3 = self.ff(torch.cat((x1, x2), dim=-1))
 
        return x3
 
class Encoder(nn.Module):
    def __init__(self, hidden_dim=256, heads=8, num_layers=1, max_batch_size=32, dropout=0.5):
        super().__init__()
 
        self.dropout = nn.Dropout(p=dropout)
 
        self.encoder = TransformerEncoder(
            model_dim=hidden_dim,
            heads=heads,
            num_layers=num_layers,
            max_batch_size=max_batch_size,
        )
 
    def forward(self, x):
        x = x + torch.zeros_like(x)
 
        # Run the Transformer encoder on the inputs
        return self.encoder(**x)
 

class TransformerEncoder(nn.Module):
    def __init__(self, model_dim=256, heads=8, num_layers=1, max_batch_size=32):
        super().__init__()
 
        # Create a new Transformer with 3 layers of multi-headed attention
        self.transformer = nn.Transformer(
            d_model=model_dim, 
            nhead=heads,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            max_seq_len=max_batch_size
        )
 
    def forward(self, x):
        # Run the Transformer encoder on the inputs
        return self.transformer(**x)
 
class TransfoHeadModel(nn.Module):
    def __init__(self, heads=128, d_model=512, max_batch_size=32):
        super().__init__()
 
        self.dropout = nn.Dropout(p=0.5)
        
        self.transformer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=heads,
            dim_feedforward=1024, 
            dropout=0.0, 
            activation='relu'
        )
 
    def forward(self, x):
        # Run the Transformer encoder on the inputs
        return self.transformer(**x)
 

class TransfoHeadModelV2(nn.Module):
    def __init__(self, heads=8, d_model=256, max_batch_size=32):
        super().__init__()
 
        self.dropout = nn.Dropout(p=0.1)
        
        # Run the Transformer encoder on the inputs
        # The default head in transformers is 8
        self.transformer = torch.nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=heads,
            dim_feedforward=512, 
            dropout=0.0, 
            activation='relu'
        )
 
    def forward(self, x):
        # Run the Transformer encoder on the inputs
        return self.transformer(**x)
 

class TransfoHeadModelV3(nn.Module):
    def __init__(self, heads=128, d_model=256, max_batch_size=32):
        super().__init__()
 
        self.dropout = nn.Dropout(p=0.5)
        
        # Run the Transformer encoder on the inputs
        self.transformer = torch.nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=heads,
            dim_feedforward=101- "
This section discus<jupyter_output><empty_output><jupyter_text>Let's take a look at the data and how it looks like<jupyter_code>df.head()
df['2017', '1'],
       ['2018', '3']]

#The index numbers in the two columns are for some reason treated 
#treatment, the rest of the data is just raw data
#I would say this has a lot of features, but it also has a really small number of records, so maybe it's not worth it.
#it could be more interesting if I did a single graph to look at things in depth for each individual
#It might also have been an idea to take the word 'treatment' and turn it into an additional category
#It might be possible to try using PCA as well, but we'll see what happens
#I think maybe the next step is to go back over what I found (or at least some of what I did) in more depth.
#And then decide if there are any further things I'd like to try or not, and whether or not it's worth the effort.<jupyter_output><empty_output><jupyter_text>How about this?<jupyter_code>#maybe use a boxplot? 
#also make sure to have a categorical y axis, because that is generally what they will want (unless you're trying to predict continuous)
#then use a color code of something related to each x-axis value
#then maybe try to use multiple colors for each unique dimensionality for the same data type

df.plot(kind='box', subplots=True, layout=(5,2),sharex=False, sharey=False)<jupyter_output><empty_output><jupyter_text>This is a bit hard to digest with just so many features, but at least we can get an idea of the general distribution of values for each column and whether or not they are highly correlated.<jupyter_code>#now let's get a little more information from this data
print(f'The total number of entries in the dataframe is {len(df)}')
#so far, that's fine but we can also figure out a lot more about what kind of data type each column contains by looking at the following statistics:
print(f"Number of unique values in each column are:\n{list(zip(*[df.columns for _ in range(len(df))]))}\n")
#that's pretty much what we were doing all this time! But let's add one more statistic that I feel will be very useful later on (if not already): the standard deviation from the mean, which is a good metric to use if you just want to know how far each feature is from the overall average.
#let's write this out ourselves, because it's quite nice:
def print_deviation(df, num_decimals=3):
    for idx in range(len(df)):
        mean = df[df.columns[idx]].mean()
        
        standard_deviation = (df[df.columns[idx]].max()-df[df.columns[idx]].min())/np.sqrt(len(df))
        print(f"The std dev for {df.columns[idx]} is {round(standard_deviation, num_decimals)}")
    return
print_deviation(df)<jupyter_output><empty_output><jupyter_text>How about some more of that info? We could get this for a specific column by doing:<jupyter_code>#selecting a random set of features to see what they are like and their distribution
#if I were using PCA, this might be different than the data we're working with now
import warnings
warnings.filterwarnings("ignore")

test_columns = df.loc[:,0]]
print(f"The first column is {test_columns[test_columns[0]].dtype}")
#that's a problem! This function will throw an error whenever there is something that it can't deal with, and we're just going to have to figure out what to do about those ourselves. If you don't like warnings, you'll need to get around them somehow. In this case, I guess we should look for NaNs and fill them in!
def nan_to_zero(df):
    return (df-df[0]) if np.isnan(df) else df
    
#and then run that function on the whole dataset:
test_columns = nan_to_zero(test_columns)<jupyter_output><empty_output><jupyter_text>Let's now see what distribution of columns these features are in!<jupyter_code>import seaborn as sns;
sns.set_style("white")
f, axarr = plt.subplots(5)
for idx in range(len(df)):
    dummies = pd.get_dummies(test_columns[idx])

    test_columns[idx] = np.array([1 if elem == True else 0 for sublist in list(dumm 