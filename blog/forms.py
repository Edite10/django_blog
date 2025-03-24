from django import forms
from .models import Post, Comment
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    # Simplify the TinyMCE configuration to fix potential issues
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 80, 'rows': 15},
            mce_attrs={
                'plugins': 'link image lists advlist'
                ' fullscreen media code table',
                'toolbar': 'undo redo | formatselect | bold '
                'italic | alignleft aligncenter alignright '
                'alignjustify | bullist numlist outdent '
                'indent | link image media | code',
                'menubar': False,
                'statusbar': True,
                'width': '100%',
                'height': 400,
            }
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3, 'placeholder':
                'Add a comment...'
            }),
        }
        labels = {
            'body': 'Comment',
        }
