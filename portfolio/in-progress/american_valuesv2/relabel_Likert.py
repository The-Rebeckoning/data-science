def relabel_likert(columns):
        """Restructures Likert scale"""
        outputs = ["Somewhat important","Not so important","Not at all important"]
        conditions = [
        np.logical_and(df['Voting'].gt(1), np.less_equal(df['Voting'], 2)),
        np.logical_and(df['Voting'].gt(2), np.less_equal(df['Voting'], 3)),
        np.logical_and(df['Voting'].gt(3), np.less_equal(df['Voting'], 4)),
        ]
        for column in columns:
                full_df[column] = pd.Series(np.select(conditions, outputs, 'Very important'))


relabel_likert