import React from 'react';
import MessagesList from './MessagesList';
import ReceiversList from './ReceiversList';
import {getReceiversList, getMessagesList} from './messagesBarService';

const messagesListStyle = {
    display: 'flex',
    flexDirection: 'column',
    position: 'absolute',
    top: 0,
    marginRight: '20%'
};

export default class MessagesBar extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            style: this.props.style,
            isMessagesList: false,
            isReceiversList: true,
            receiversListExpandedWidth: this.props.expandedWidth,
            receiversListWrappedWidth: this.props.wrappedWidth,
            activeReceiverItem: -1
        };

    }
    componentWillMount() {
        const receiversObject = this.props.location === 'progress' ? getReceiversList() : getReceiversList(true);
        this.setState({
            receivers: receiversObject.receivers
        });
    }

    handleReceiverClick = receiverId => {
        this.setState({
            isMessagesList: true,
            isReceiversList: false,
            messages: getMessagesList(receiverId).messages,
            activeReceiverItem: receiverId
        });
    };

    handleReceiversListMouseOver = () => {
        this.setState({
            isReceiversList: true
        });
    };

    handleReceiversListMouseLeave = () => {
        this.setState({
            isReceiversList: false
        });
    };

    render() {

        let messagesList = this.state.isMessagesList ?
            <MessagesList messages={this.state.messages} style={messagesListStyle} /> :
            null;

        return (
            <div style={this.state.style}>
                <ReceiversList
                    receivers={this.state.receivers}
                    isExpanded={this.state.isReceiversList}
                    expandedWidth={this.state.receiversListExpandedWidth}
                    wrappedWidth={this.state.receiversListWrappedWidth}
                    onReceiverClick={this.handleReceiverClick}
                    onMouseOver={this.handleReceiversListMouseOver}
                    onMouseLeave={this.handleReceiversListMouseLeave}
                    activeReceiverItem={this.state.activeReceiverItem}
                />
                {messagesList}
            </div>
        );
    }
}