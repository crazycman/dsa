import React from 'react'
import { Header, List } from 'semantic-ui-react'

export const Orgnizations = ({orgs}) => {
    return (
        <List>
            {orgs.map(org => {
                return (
                    <List.Item key={org.name}>
                        <Header>{org.name}</Header>
                        <List.List>
                            {org.members.map(m => {
                                return (
                                    <List.Item key={m}>
                                        {m}
                                    </List.Item>
                                )
                            })}
                        </List.List>
                    </List.Item>
                )
            })}
        </List>        
    )
}