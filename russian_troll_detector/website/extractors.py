from sklearn.base import BaseEstimator, TransformerMixin

class ColumnExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, vars):
        self.vars = vars  # e.g. pass in a column name to extract

    def transform(self, X, y=None):
        return X[self.vars]  # where the actual feature extraction happens

    def fit(self, X, y=None):
        return self  # generally does nothing


class TextExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, vars):
        self.vars = vars  # e.g. pass in a column name to extract

    def transform(self, X, y=None):
        return X[self.vars]  # where the actual feature extraction happens

    def fit(self, X, y=None):
        return self  # generally does nothing
